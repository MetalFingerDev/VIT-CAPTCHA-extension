// content.js


// Waits for element to load
function waitForElement(selector) {
  return new Promise(resolve => {
    if (document.querySelector(selector)) {
      return resolve(document.querySelector(selector));
    }

    const observer = new MutationObserver(mutations => {
      if (document.querySelector(selector)) {
        resolve(document.querySelector(selector));
        observer.disconnect();
      }
    });

    observer.observe(document.body, {
      childList: true,
      subtree: true
    });
  });
}

// Handles capturing image & sending to the API
async function handleCaptcha(imageElement, inputElement) {
  const base64Image = imageElement.src;

  if (base64Image) {
    console.log("CAPTCHA image data captured. Sending to API...");
    
    // Checks if the extension context is still valid
    if (chrome.runtime && chrome.runtime.id) {
      // Sends message to the background.js with image data
      chrome.runtime.sendMessage({ action: "solveCaptcha", imageData: base64Image }, (response) => {
        if (response && response.solution) {
          console.log("CAPTCHA solved:", response.solution);
          fillForm(inputElement, response.solution);
        } else {
          console.error("Failed to get CAPTCHA solution.");
        }
      });
    } else {
      console.error("Extention context invalidated. Cannot send message")
    }
  } else {
    console.error("Could not capture the CAPTCHA image data.");
  }
}

// Fills the input field
function fillForm(inputElement, solution) {
  if (inputElement) {
    inputElement.value = solution;
    console.log("CAPTCHA filled");
  } else {
    console.error("The CAPTCHA input field or submit button was not found.");
  }
}


// --- Main execution logic ---

// async IIFE (Immediately Invoked Function Expression)
async function findCaptchaElements() {
    const captchaContainer = await waitForElement('.col-7.mx-auto');
    const captchaInput = document.querySelector('#captchaStr');
    
    if (captchaContainer && captchaInput) {
        console.log("Found all required elements. Proceeding with CAPTCHA solving.");
        
        // 1. Solve CAPTCHA on detection
        const solveNewCaptcha = () => {
          const newCaptchaImage = captchaContainer.querySelector('img.form-control.img-fluid.bg-light.border-0')
          if (newCaptchaImage) {
            console.log("New CAPTCHA detected.")
            handleCaptcha(newCaptchaImage, captchaInput);
          }
        };
        solveNewCaptcha();

        // 2. Set up a MutationObserver to watch for refreshes
        const observer = new MutationObserver(() => {
          solveNewCaptcha();
        });

        // Configure the observer to watch for attribute changes on the image element
        const config = { childList: true, subtree: true };
        observer.observe(captchaContainer, config);
        console.log("Observing CAPTCHA container for changes...");
    } else {
        console.error("Could not find one or more required elements.");
    }
}

// calling main funtion
findCaptchaElements();
