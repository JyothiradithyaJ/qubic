console.log(" Analytics JS Loading");

const API = "http://127.0.0.1:8000";

// MAIN FUNCTION
async function loadAnalytics() {

    let res = await fetch(`${API}/routine/list`);
    let json = await res.json();

    console.log(" Data Received from backend:", json);

    // Handle different possible backend formats
    let data = json.routine_logs || json || [];

    if (!Array.isArray(data)) {
        console.error(" ERROR: Expected array but got:", data);
        return;
    }

    let study = {};
    let screen = {};
    let dist = {};

    // Loop through routine logs
    data.forEach(r => {

        // Fix missing or malformed timestamps
        let date = "Unknown";
        if (r.timestamp) {
            try {
                date = r.timestamp.split("T")[0];
            } catch (err) {
                date = "Unknown";
            }
        }

        let act = (r.activity || "").toLowerCase();

        // Activity Distribution
        dist[r.activity] = (dist[r.activity] || 0) + r.duration;

        // Study Trend
        if (act === "study") {
            study[date] = (study[date] || 0) + r.duration;
        }

        // Screen Trend
        if (act === "screen") {
            screen[date] = (screen[date] || 0) + r.duration;
        }
    });

    buildStudyChart(study);
    buildScreenChart(screen);
    buildDistChart(dist);
}

/* -------------------------------
   CHART BUILDERS
---------------------------------*/

function buildStudyChart(study) {
    new Chart(document.getElementById("studyChart"), {
        type: "line",
        data: {
            labels: Object.keys(study),
            datasets: [{
                label: "Study Minutes",
                data: Object.values(study),
                borderColor: "cyan",
                backgroundColor: "rgba(0,255,255,0.20)",
                borderWidth: 3,
                tension: 0.3,
                pointRadius: 5,
                pointBackgroundColor: "cyan"
            }]
        },
        options: {
            plugins: { legend: { labels: { color: "white" } } },
            scales: {
                x: { ticks: { color: "white" } },
                y: { ticks: { color: "white" } }
            }
        }
    });
}

function buildScreenChart(screen) {
    new Chart(document.getElementById("screenChart"), {
        type: "bar",
        data: {
            labels: Object.keys(screen),
            datasets: [{
                label: "Screen Minutes",
                data: Object.values(screen),
                backgroundColor: "rgba(255,165,0,0.8)",
                borderColor: "orange",
                borderWidth: 2
            }]
        },
        options: {
            plugins: { legend: { labels: { color: "white" } } },
            scales: {
                x: { ticks: { color: "white" } },
                y: { ticks: { color: "white" } }
            }
        }
    });
}

function buildDistChart(dist) {
    new Chart(document.getElementById("distChart"), {
        type: "doughnut",
        data: {
            labels: Object.keys(dist),
            datasets: [{
                data: Object.values(dist),
                backgroundColor: [
                    "cyan", "orange", "violet", "lime", "pink"
                ],
                borderColor: "#fff",
                borderWidth: 2
            }]
        },
        options: {
            plugins: { legend: { labels: { color: "white" } } }
        }
    });
}

loadAnalytics();

