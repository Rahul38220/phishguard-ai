function waitForEmailBody(retries = 10) {
    return new Promise((resolve) => {
        let attempt = 0;

        const interval = setInterval(() => {
            const body = document.querySelector("div.a3s");
            const sender = document.querySelector(".gD")?.getAttribute("email") || "unknown@example.com";

            if (body || attempt >= retries) {
                clearInterval(interval);
                resolve({
                    text: body ? body.innerText : null,
                    sender: sender
                });
            }

            attempt++;
        }, 1000);
    });
}

chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.action === "scan_email") {
        waitForEmailBody().then(data => {
            sendResponse(data);
        });
        return true; // Required for async response
    }
});
