const chatBox = document.getElementById("chat-box");
const input = document.getElementById("userInput");

async function sendMessage() {
    const message = input.value;
    if (!message) return;
    addMessage("🧑 You: " + message);

    const res = await fetch("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message }),
    });

    const data = await res.json();
    addMessage("🤖 Bot: " + data.reply);
    speakText(data.reply);

    input.value = "";
}

function addMessage(text) {
    const p = document.createElement("p");
    p.textContent = text;
    chatBox.appendChild(p);
    chatBox.scrollTop = chatBox.scrollHeight;
}

// 🎤 Voice input using Web Speech API
function speak() {
    const recognition = new webkitSpeechRecognition();
    recognition.lang = "en-US";
    recognition.start();

    recognition.onresult = (event) => {
        const userText = event.results[0][0].transcript;
        input.value = userText;
        sendMessage();
    };
}

// 🔊 Bot voice output
function speakText(text) {
    const speech = new SpeechSynthesisUtterance(text);
    speech.rate = 1;
    speech.pitch = 1;
    window.speechSynthesis.speak(speech);
}
