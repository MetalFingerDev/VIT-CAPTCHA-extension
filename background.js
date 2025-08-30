// background.js


chrome.runtime.onMessage.addListener((request, _ , sendResponse) => {
  if (request.action === "solveCaptcha") {
    // URL for API endpoint
    const apiUrl = "http://127.0.0.1:8008/api/solve"; 

    // Extracts the base64 data from the image source
    const imageData = request.imageData.split(',')[1];

    // Sends a POST request to API
    fetch(apiUrl, {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ image: imageData })
    })
    .then(response => response.json())
    .then(data => {
      // Checks if the API returned a solution
      if (data && data.solution) {
        console.log("CAPTCHA solved by your Flask API:", data.solution);
        sendResponse({ solution: data.solution });
      } else {
        console.error("API did not return a valid solution:", data.error);
        sendResponse({ error: "API error" });
      }
    })
    .catch(error => {
      console.error("Network error with API:", error);
      sendResponse({ error: "Network error" });
    });
    
    // Return true to indicate  asynchronous response
    return true; 
  }
});
