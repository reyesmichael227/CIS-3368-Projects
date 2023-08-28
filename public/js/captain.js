// Add captain WORKING
document.getElementById('add-captain-form').addEventListener('submit', async (event) => {
  event.preventDefault();
  
  // Get the form data
  const formData = new FormData(event.target);
  // Create an object with the form data
  const data = Object.fromEntries(formData.entries());
  
  const response = await axios.post('/captain', data);
  console.log(response);
  const resultDiv = document.getElementById('result');
  resultDiv.innerHTML = response.data;
  alert('Add captain successful.');
  location.reload('');
 
});



// Update Captain
document.getElementById('update-captain-form').addEventListener('submit', async (event) => {
  event.preventDefault();

  // Get the form data
  const formData = new FormData(event.target);

  // Create an object with the form data
  const data = {
    id: formData.get('update-id'), // Extract the cargo ID from the form data
    firstname: formData.get('update-firstname'),
    lastname: formData.get('update-lastname'),
    captainrank: formData.get('update-captainrank'),
    homeplanet: formData.get('update-homeplanet')
  };

  // Make the PUT request to update the captain
  const response = await axios.put('/captain', data);
  console.log(response);
  alert('Update captain successful.');
  location.reload('');
});

// Delete captain
document.getElementById('delete-captain-form').addEventListener('submit', async (event) => {
  event.preventDefault();
  // Get the form data
  const formData = new FormData(event.target);
  // Create an object with the form data
  const data = Object.fromEntries(formData.entries());
  
  try {
      const response = await axios.delete('http://127.0.0.1:5000/api/captain/delete', { data });
      console.log(response);
      alert('Delete captain successful.');
      location.reload();
  } catch (error) {
      console.error(error);
      alert('Failed to delete captain.');
  }
});

