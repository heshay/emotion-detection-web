const analyzeButton = document.getElementById("analyzeButton");
const textInput = document.getElementById("textInput");

const result = document.getElementById("result");
const emotion = document.getElementById("emotion");
const confidence = document.getElementById("confidence");
const progressBar = document.getElementById("progressBar");

const charCount = document.getElementById("charCount");

const sadnessProbability =
    document.getElementById("sadnessProbability");

const joyProbability =
    document.getElementById("joyProbability");

const angerProbability =
    document.getElementById("angerProbability");

const sadnessBar =
    document.getElementById("sadnessBar");

const joyBar =
    document.getElementById("joyBar");

const angerBar =
    document.getElementById("angerBar");


// =========================
// CHARACTER COUNTER
// =========================

textInput.addEventListener("input", () => {

    charCount.textContent =
        textInput.value.length;

});


// =========================
// ANALYZE BUTTON
// =========================

analyzeButton.addEventListener("click", async () => {

    const text = textInput.value.trim();


    // Make sure the user entered something

    if (text === "") {

        alert("Please enter some text.");

        return;

    }


    // Disable button while analyzing

    analyzeButton.disabled = true;

    analyzeButton.textContent =
        "Analyzing...";


    try {

        // Send text to Flask

        const response = await fetch("/predict", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                text: text
            })

        });


        // Get prediction from Flask

        const data = await response.json();


        // =========================
        // EMOTION
        // =========================

        emotion.textContent =
            data.emotion;


        // =========================
        // CONFIDENCE
        // =========================

        const confidencePercent =
            Math.round(data.confidence * 100);


        confidence.textContent =
            confidencePercent + "%";


        progressBar.style.width =
            confidencePercent + "%";


        // =========================
        // PROBABILITIES
        // =========================

        const sadnessPercent =
            Math.round(
                data.probabilities.sadness * 100
            );

        const joyPercent =
            Math.round(
                data.probabilities.joy * 100
            );

        const angerPercent =
            Math.round(
                data.probabilities.anger * 100
            );


        // =========================
        // PROBABILITY NUMBERS
        // =========================

        sadnessProbability.textContent =
            sadnessPercent + "%";

        joyProbability.textContent =
            joyPercent + "%";

        angerProbability.textContent =
            angerPercent + "%";


        // =========================
        // PROBABILITY BARS
        // =========================

        sadnessBar.style.width =
            sadnessPercent + "%";

        joyBar.style.width =
            joyPercent + "%";

        angerBar.style.width =
            angerPercent + "%";


        // =========================
        // SHOW RESULTS
        // =========================

        result.classList.remove("hidden");


    } catch (error) {

        console.error(error);

        alert("Something went wrong.");

    }


    // Enable button again

    analyzeButton.disabled = false;

    analyzeButton.textContent =
        "▶ ANALYZE EMOTION";

});