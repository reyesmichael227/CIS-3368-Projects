// Add Cargo WORKING
document.getElementById('add-cargo-form').addEventListener('submit', async (event) => {
  event.preventDefault();
  
  // Get the form data
  const formData = new FormData(event.target);
  // Create an object with the form data
  const data = Object.fromEntries(formData.entries());
  
  const response = await axios.post('/cargo', data);
  console.log(response);
  const resultDiv = document.getElementById('result');
  resultDiv.innerHTML = response.data;
  alert('Add cargo successful.');
  location.reload('');
  
});

// Update Cargo
document.getElementById('update-cargo-form').addEventListener('submit', async (event) => {
  event.preventDefault();

  // Get the form data
  const formData = new FormData(event.target);

  // Create an object with the form data
  const data = {
    id: formData.get('cargo-id'), // Extract the cargo ID from the form data
    weight: formData.get('new-weight'),
    cargotype: formData.get('new-cargotype'),
    departure: formData.get('new-departure'),
    shipid: formData.get('new-shipid')
  };

  // Make the PUT request to update the cargo
  const response = await axios.put('/cargo', data);
  console.log(response);
  alert('Update cargo successful.');
  location.reload();
});

// Delete Cargo called via app
document.getElementById('delete-cargo-form').addEventListener('submit', async (event) => {
  event.preventDefault();
  // Get the form data
  const formData = new FormData(event.target);
  // Create an object with the form data
  const data = Object.fromEntries(formData.entries());
  
  const response = await axios.delete('http://127.0.0.1:5000/api/cargo/delete', { data });
  console.log(response);
  alert('Delete cargo successful.');
  location.reload();
});

