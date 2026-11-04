
function updateTimers() {

    // Select all deadline elements on the page
    const deadlines = document.querySelectorAll(".deadline-date");

    deadlines.forEach(function(deadline) {

        // Get the deadline date from HTML
        const deadlineDate = deadline.dataset.deadline;

        // Find the countdown element
        const timer = deadline.parentElement.querySelector(".countdown");

        if (!deadlineDate || !timer) {
            return;
        }

        // Convert the date into year, month and day
        const [year, month, day] = deadlineDate.split("-").map(Number);

        // Set deadline to the end of that day
        const targetDate = new Date(year, month - 1, day, 23, 59, 59);

        // Get current date and time
        const now = new Date();

        // Calculate remaining milliseconds
        const remaining = targetDate - now;

        // Remove previous warning colours
        deadline.classList.remove("urgent", "warning", "overdue");
        timer.classList.remove("urgent", "warning", "overdue");

        // Check whether deadline has passed
        if (remaining < 0) {

            deadline.classList.add("overdue");
            timer.classList.add("overdue");

            timer.textContent = "Overdue";

            return;
        }

        // Calculate remaining days
        const days = Math.floor(
            remaining / (1000 * 60 * 60 * 24)
        );

        // Calculate remaining hours
        const hours = Math.floor(
            (remaining / (1000 * 60 * 60)) % 24
        );

        // Calculate remaining minutes
        const minutes = Math.floor(
            (remaining / (1000 * 60)) % 60
        );

        // Calculate remaining seconds
        const seconds = Math.floor(
            (remaining / 1000) % 60
        );

        // Display the countdown
        timer.textContent =
            `${days}d ${hours}h ${minutes}m ${seconds}s`;

        // RED: 2 days or less remaining
        if (remaining <= 2 * 24 * 60 * 60 * 1000) {

            deadline.classList.add("urgent");
            timer.classList.add("urgent");

        }

        // YELLOW: More than 2 days but 7 days or less
        else if (remaining <= 7 * 24 * 60 * 60 * 1000) {

            deadline.classList.add("warning");
            timer.classList.add("warning");

        }

    });

}

// Run immediately when page loads
updateTimers();

// Update countdown every second
setInterval(updateTimers, 1000);
