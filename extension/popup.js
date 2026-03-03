
document.getElementById("scan").addEventListener("click", async () => {
  chrome.tabs.query({ active: true, currentWindow: true }, tabs => {
    chrome.tabs.sendMessage(tabs[0].id, { action: "scan_email" }, async response => {
      if (!response) {
        document.getElementById("result").innerText = "No email content found.";
        return;
      }
      const classify = await fetch("http://localhost:8000/classify", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text: response.text })
      });
      const cls = await classify.json();

      let resultText = `Result: ${cls.label}`;
      if (cls.label === "phishing") {
        const explain = await fetch("http://localhost:8000/explain", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ text: response.text })
        });
        const exp = await explain.json();
        resultText += `\n\nWhy? ${exp.explanation}`;

        // Save sender locally
        let scamSenders = JSON.parse(localStorage.getItem("scam_senders") || "[]");
        if (!scamSenders.includes(response.sender)) {
          scamSenders.push(response.sender);
          localStorage.setItem("scam_senders", JSON.stringify(scamSenders));
        }
      }

      document.getElementById("result").innerText = resultText;
    });
  });
});
