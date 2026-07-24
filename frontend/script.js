const API_URL = "https://page-pulse-uajo.onrender.com/audit";


async function auditURL() {

    const urlInput = document.getElementById("urlInput");
    const result = document.getElementById("result");

    const url = urlInput.value.trim();


    if (!url) {
        result.textContent = "Please enter a URL.";
        return;
    }


    result.textContent = "Running audit...";


    try {

        const response = await fetch(API_URL, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                url: url
            })
        });


        const data = await response.json();


        if (!response.ok) {
            result.textContent = JSON.stringify(
                data,
                null,
                2
            );
            return;
        }


        result.textContent = JSON.stringify(
            data,
            null,
            2
        );


    } catch (error) {

        console.error("API Error:", error);

        result.textContent =
            "Unable to connect to Page Pulse API.\n\n" +
            error.message;

    }
}
