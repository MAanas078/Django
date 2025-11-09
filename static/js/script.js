// Theme Toggle
const toggleBtn = document.getElementById('toggle-theme');
const body = document.getElementById('body');
const icon = toggleBtn.querySelector('i');

toggleBtn.addEventListener('click', () => {
  body.classList.toggle('dark-mode');
  if (body.classList.contains('dark-mode')) {
    icon.classList.replace('bi-moon', 'bi-sun');
    toggleBtn.classList.replace('btn-dark', 'btn-light');
  } else {
    icon.classList.replace('bi-sun', 'bi-moon');
    toggleBtn.classList.replace('btn-light', 'btn-dark');
  }
});

// Delete Confirmation Modal
function confirmDelete(taskId) {
  const deleteLink = document.getElementById('deleteLink');
  deleteLink.href = `/delete/${taskId}/`;
  const modal = new bootstrap.Modal(document.getElementById('deleteModal'));
  modal.show();
}
