// static/js/chart.js
document.addEventListener('DOMContentLoaded', function() {
    fetch('/chart-data/')
        .then(response => response.json())
        .then(data => {
            new Chart("myChart", {
                type: "bar",
                data: {
                    labels: data.labels,
                    datasets: [{
                        backgroundColor: "#df4a32",
                        data: data.values
                    }]
                },
                options: {
                    legend: { display: false },
                    title: {
                        display: true,
                        text: "World Wine Production 2018"
                    }
                }
            });
        });
});