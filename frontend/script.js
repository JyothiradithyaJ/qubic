




const API = "http://127.0.0.1:8000";

// Add Task
async function addTask() {
    let title = document.getElementById("title").value;
    let deadline = document.getElementById("deadline").value;
    let priority = parseInt(document.getElementById("priority").value);

    await fetch(`${API}/tasks/add`, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({title, deadline, priority})
    });

    alert("Task added!");
}

// Load Tasks
async function loadTasks() {
    let res = await fetch(`${API}/tasks/list`);
    let data = await res.json();
    console.log("Received from backend:", data);


let tasks = data.tasks;   // <-- the array is inside "tasks"

    console.log("Received from backend:", tasks);

    let html = "";
    

    tasks.forEach(t => {
        html += `
        <div class="glass p-5 rounded-xl flex justify-between items-center">
            <div>
                <div class="text-xl font-semibold">${t.title}</div>
                <div class="text-gray-300 text-sm">Priority: ${t.priority}</div>
                <div class="text-gray-400 text-sm">Deadline: ${t.deadline}</div>
            </div>

            <button onclick="deleteTask(${t.id})"
                class="p-2 bg-red-500 rounded glow">
                Delete
            </button>
        </div>`;
    });

    document.getElementById("taskList").innerHTML = html;
}

// Delete task
async function deleteTask(id) {
    await fetch(`${API}/tasks/delete/${id}`, { method: "DELETE" });
    loadTasks();
}

// AI Recommendations
async function getRecommendations() {
    let res = await fetch(`${API}/recommend/`);
    let data = await res.json();

    let output = document.getElementById("output");
    output.classList.remove("hidden");

    output.innerHTML = `
        <h2 class="text-2xl font-bold mb-4">AI Insights</h2>
        <pre>${JSON.stringify(data, null, 2)}</pre>
    `;
}
