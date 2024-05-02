const chatBox = document.getElementById("chat-messages");
const userInput = document.getElementById("user-input");
const initial = document.querySelector('.initial-box');

userInput.addEventListener("keypress", function(event) {
    if (event.keyCode === 13) {
        sendMessage();
    }
});

function sendMessage() {
    if(initial.style.display == ''){
        initial.style.display = 'none';
    }
    const userMessage = userInput.value.trim();
    if (userMessage !== "") {
        displayMessage(userMessage, "user");
        fetch('http://127.0.0.1:5000/process_text', {
            method: 'POST',
            body: JSON.stringify({ "text": userMessage }),
            headers: {
                'Content-Type': 'application/json'
            }
        })
        .then(response => response.json())
        .then(data => {
            displayMessage(data.output_text, "bot");
            scrollToBottom(); // Scroll to bottom after displaying bot message
        })
        .catch(error => console.error('Error:', error));
        userInput.value = "";
    }
}

function displayMessage(msg, sender) {
    const messageElement = document.createElement("div");
    messageElement.classList.add(sender+"-msg-disp");
    const message = document.createElement("div");
    message.classList.add(sender + "-message");
    message.innerText = msg;
    const imgtag = document.createElement("img");
    imgtag.src = `./assets/${sender}.png`;
    imgtag.classList.add("logo");
    messageElement.appendChild(imgtag);
    messageElement.appendChild(message);
    chatBox.appendChild(messageElement);
}

function scrollToBottom() {
    chatBox.scrollTop = chatBox.scrollHeight;
}