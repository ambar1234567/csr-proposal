// Simplified Chart.js for CSR Proposal Scoring Radar Chart
document.addEventListener('DOMContentLoaded', function() {
    // Only initialize if we're on the results page
    if (document.getElementById('scoreChart')) {
        const ctx = document.getElementById('scoreChart').getContext('2d');
        
        // Chart data from the template
        const chartData = {
            labels: ['Language', 'Literature', 'Presentation', 'Risk', 'Budget'],
            datasets: [{
                label: 'Proposal Scores',
                data: [
                    {{ result.scores.Language }},
                    {{ result.scores['Literature Review'] }},
                    {{ result.scores.Presentation }},
                    {{ result.scores['Risk Mitigation'] }},
                    {{ result.scores.Budget }}
                ],
                backgroundColor: 'rgba(54, 162, 235, 0.2)',
                borderColor: 'rgba(54, 162, 235, 1)',
                pointBackgroundColor: 'rgba(54, 162, 235, 1)',
                pointBorderColor: '#fff',
                pointHoverRadius: 5,
                pointHoverBackgroundColor: '#fff',
                pointHoverBorderColor: 'rgba(54, 162, 235, 1)'
            }]
        };

        // Chart configuration
        const config = {
            type: 'radar',
            data: chartData,
            options: {
                scales: {
                    r: {
                        angleLines: {
                            display: true,
                            color: 'rgba(200, 200, 200, 0.3)'
                        },
                        suggestedMin: 0,
                        suggestedMax: 20,
                        ticks: {
                            stepSize: 5,
                            backdropColor: 'transparent'
                        }
                    }
                },
                plugins: {
                    legend: {
                        display: false
                    },
                    tooltip: {
                        callbacks: {
                            label: function(context) {
                                return `${context.dataset.label}: ${context.raw}/20`;
                            }
                        }
                    }
                },
                elements: {
                    line: {
                        tension: 0.1
                    }
                }
            }
        };

        new Chart(ctx, config);
    }
});