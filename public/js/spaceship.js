// Add spaceship WORKING
document.getElementById('add-spaceship-form').addEventListener('submit', async (event) => {
  event.preventDefault();
  
  // Get the form data
  const formData = new FormData(event.target);
  // Create an object with the form data
  const data = Object.fromEntries(formData.entries());
  
  const response = await axios.post('/spaceship', data);
  console.log(response);
  const resultDiv = document.getElementById('result');
  resultDiv.innerHTML = response.data;
  alert('Add spaceship successful.');
  location.reload('');
  
});


// Update spaceship
document.getElementById('update-spaceship-form').addEventListener('submit', async (event) => {
  event.preventDefault();
  // Get the form data
  const formData = new FormData(event.target);
  // Create an object with the form data
  const data = Object.fromEntries(formData.entries());
  
  try {
      const response = await axios.put('http://127.0.0.1:5000/api/spaceship/put', data);
      console.log(response);
      alert('Update spaceship successful.');
      location.reload();
  } catch (error) {
      console.error(error);
      alert('Failed to update spaceship.');
  }
});

// Delete spaceship
document.getElementById('delete-spaceship-form').addEventListener('submit', async (event) => {
  event.preventDefault();
  // Get the form data
  const formData = new FormData(event.target);
  // Create an object with the form data
  const data = Object.fromEntries(formData.entries());
  
  try {
      const response = await axios.delete('http://127.0.0.1:5000/api/spaceship/delete', { data });
      console.log(response);
      alert('Delete spaceship successful.');
      location.reload();
  } catch (error) {
      console.error(error);
      alert('Failed to delete spaceship.');
  }
});

