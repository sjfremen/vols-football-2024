// Sample data loading
document.addEventListener('DOMContentLoaded', function() {
    const tableBody = document.getElementById('data-table').getElementsByTagName('tbody')[0];

    fetch('summary_data.csv') // Adjusted path if necessary
        .then(response => response.text())
        .then(data => {
            const rows = data.split('\n');
            const headers = rows[0].split(','); // Assuming first row contains headers
            
            // Start from the second row (index 1) to skip headers
            for (let i = 1; i < rows.length; i++) {
                const cols = rows[i].split(',');
                if (cols.length === headers.length) { // Ensure valid row
                    const newRow = tableBody.insertRow();
                    const playTypeIndex = headers.indexOf('Play Type'); // Get index for "Play Type"
                    const countIndex = headers.indexOf('Count'); // Get index for "Count"

                    // Insert cells for Play Type and Count
                    if (playTypeIndex > -1) {
                        const playTypeCell = newRow.insertCell();
                        playTypeCell.textContent = cols[playTypeIndex];
                    }

                    if (countIndex > -1) {
                        const countCell = newRow.insertCell();
                        countCell.textContent = cols[countIndex];
                    }
                }
            }
        })
        .catch(error => {
            console.error('Error loading the CSV file:', error);
        });
});
