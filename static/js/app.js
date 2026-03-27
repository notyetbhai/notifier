function updateTimers() {
    const timers = document.querySelectorAll('.timer-container');
    
    timers.forEach(container => {
        const expiryDateStr = container.dataset.expiry;
        const expiryDate = new Date(expiryDateStr);
        const now = new Date();
        const diffMs = expiryDate - now;
        
        const textEl = container.querySelector('.timer-text');
        const statusEl = container.querySelector('.timer-status');
        const barEl = container.querySelector('.timer-bar');
        
        // Remove old color classes
        container.classList.remove('text-primary', 'text-[#ffc107]', 'text-error', 'text-outline');
        barEl.classList.remove('bg-primary', 'bg-[#ffc107]', 'bg-error', 'bg-outline-variant');
        
        if (diffMs <= 0) {
            textEl.textContent = "0D";
            statusEl.textContent = "EXPIRED";
            container.classList.add('text-outline');
            barEl.classList.add('bg-outline-variant');
            barEl.style.width = '100%';
            return;
        }
        
        const days = Math.floor(diffMs / (1000 * 60 * 60 * 24));
        const hours = Math.floor((diffMs / (1000 * 60 * 60)) % 24);
        
        textEl.textContent = `${days}d ${hours}h`;
        
        let percentage = (days / 30) * 100;
        if (percentage > 100) percentage = 100;
        barEl.style.width = `${percentage}%`;
        
        if (days >= 7) {
            statusEl.textContent = "SECURE";
            container.classList.add('text-primary');
            barEl.classList.add('bg-primary');
        } else if (days >= 1) {
            statusEl.textContent = "WARNING";
            container.classList.add('text-[#ffc107]');
            barEl.classList.add('bg-[#ffc107]');
        } else {
            statusEl.textContent = "CRITICAL";
            container.classList.add('text-error');
            barEl.classList.add('bg-error');
        }
    });
}

function revealPassword(id) {
    const pwSpan = document.getElementById(`pw-${id}`);
    
    if (pwSpan.dataset.revealed === "true") {
        pwSpan.textContent = "••••••••••••••••";
        pwSpan.dataset.revealed = "false";
        return;
    }
    
    pwSpan.textContent = "Decrypting...";
    
    fetch(`/api/entries/${id}/reveal`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' }
    })
    .then(res => {
        if (!res.ok) throw new Error("Unauthorized");
        return res.json();
    })
    .then(data => {
        pwSpan.textContent = data.password;
        pwSpan.dataset.revealed = "true";
    })
    .catch(err => {
        pwSpan.textContent = "Error";
        setTimeout(() => pwSpan.textContent = "••••••••••••••••", 2000);
    });
}

function copyPassword(id) {
    const pwSpan = document.getElementById(`pw-${id}`);
    if (pwSpan.dataset.revealed !== "true") {
        alert("Please reveal the password first before copying.");
        return;
    }
    copyToClipboard(pwSpan.textContent);
}

function copyToClipboard(text) {
    navigator.clipboard.writeText(text).then(() => {
        // Optional visual feedback
        console.log('Copied!');
    });
}

function deleteEntry(id) {
    if(!confirm("Are you sure you want to hard delete this entry? This action cannot be undone.")) return;
    
    fetch(`/api/entries/${id}`, {
        method: 'DELETE'
    })
    .then(res => {
        if(res.ok) window.location.reload();
        else alert("Failed to delete entry");
    });
}

// Modal Logic
function openModal() {
    document.getElementById('addModal').classList.remove('hidden');
    document.getElementById('addModal').classList.add('flex');
}

function closeModal() {
    document.getElementById('addModal').classList.add('hidden');
    document.getElementById('addModal').classList.remove('flex');
    document.getElementById('addEntryForm').reset();
}

window.addEventListener('DOMContentLoaded', () => {
    updateTimers();
    setInterval(updateTimers, 60000); // update every minute
    
    const addForm = document.getElementById('addEntryForm');
    if (addForm) {
        addForm.addEventListener('submit', function(e) {
            e.preventDefault();
            const formData = new FormData(addForm);
            const data = Object.fromEntries(formData.entries());
            
            fetch('/api/entries', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(data)
            })
            .then(res => {
                if(res.ok) {
                    closeModal();
                    window.location.reload();
                } else {
                    alert("Error saving entry");
                }
            });
        });
    }
});
