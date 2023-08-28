const express = require('express');
const path = require('path');
const bodyParser = require('body-parser');
const axios = require('axios');
const ejs = require('ejs');

const app = express();

// Set view engine to EJS
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

//setup public folder
app.use(express.static('./public'));
// parse application/x-www-form-urlencoded
app.use(bodyParser.urlencoded({ extended: false }));
// parse application/json
app.use(bodyParser.json());

// calls the login page and sets username and password and set the cargo.ejs as home page
const authenticate = async (username, password) => {
  const user = {
    id: 1,
    username: 'user', //master username
    password: 'password', //master password
  };

  if (username === user.username && password === user.password) {
    return user;
  } else {
    return null;
  }
};

// calls and renders the login page
app.get('/', (req, res) => {
  res.render('login');
});

// calls the login.ejs
app.post('/login', async (req, res) => {
  const username = req.body.username;
  const password = req.body.password;

  const user = await authenticate(username, password);
  if (user) {
    // when user logs in sucessfully is directed to cargo.esj
    res.redirect('/cargo');
  } else {
    // when user logs in sucessfully is directed to  error message
    res.render('login', { error: 'Invalid username or password' });
  }
});

// calls the cargo page
const cargoEndpoint1 = 'http://127.0.0.1:5000/api/cargo';

app.get('/cargo', async (req, res) => {
  try {
    const response = await axios.get(cargoEndpoint1);

    res.render('cargo', { cargo: response.data });
    console.log(response.data);
  } catch (error) {
    console.error(error);
    res.status(500).send('Error fetching cargo data');
  }
});

// creates a form to request then post
const cargoEndpoint2 = 'http://127.0.0.1:5000/api/cargo/post';

app.post('/cargo', async (req, res) => {
  try {
    const { weight, cargotype, departure, arrival, shipid } = req.body;

    const response = await axios.post(cargoEndpoint2, {
      weight,
      cargotype,
      departure,
      arrival,
      shipid
    });

    res.json(response.data);
  } catch (error) {
    console.error(error);
    res.status(500).send('Server Error');
  }
});

// Route to handle the cargo update form submission
const cargoEndpoint3 = 'http://127.0.0.1:5000/api/cargo/put';

app.put('/cargo', async (req, res) => {
  try {
    const { id, weight, cargotype, departure, arrival, shipid } = req.body;

    const response = await axios.put(cargoEndpoint3, {
      id,
      weight,
      cargotype,
      departure,
      arrival,
      shipid
    });

    res.json(response.data);
  } catch (error) {
    console.error(error);
    res.status(500).send('Server Error');
  }
});

//route to delete from cargo
const cargoEndpoint4 = 'http://127.0.0.1:5000/api/cargo/';

app.delete('/cargo/:id', async (req, res) => {
  try {
    const cargoId = req.params.id;
    const response = await axios.delete(cargoEndpoint4 + cargoId);

    res.json(response.data);
  } catch (error) {
    console.error(error);
    res.status(500).send('Server Error');
  }
});

// Captain page
//Captain GET Method
const captainEndpoint = 'http://127.0.0.1:5000/api/captain';
app.get('/captain', async (req, res) => {
  try {
    const response = await axios.get(captainEndpoint);

    res.render('captain', { captain: response.data });
    console.log(response.data);
  } catch (error) {
    console.error(error);
    res.status(500).send('Error fetching captain data');
  }
});

// The POST Method
const captainEndpoint1 = 'http://127.0.0.1:5000/api/captain';

app.post('/captain', async (req, res) => {
  try {
    const newCaptain = {
      firstname: req.body.firstname,
      lastname: req.body.lastname,
      captainrank: req.body.captainrank,
      homeplanet: req.body.homeplanet,
    };

    const response = await axios.post(`${captainEndpoint1}/post`, newCaptain);

    res.status(200).json(response.data);
  } catch (error) {
    console.error(error);
    res.status(500).send('Server Error');
  }
});

// This is the PUT/Update Method 
const captainEndpoint2 = 'http://127.0.0.1:5000/api/captain';

app.put('/captain/id', async (req, res) => {
  try {
    const id = req.params.id;
    const updatedCaptain = {
      firstname: req.body.firstname,
      lastname: req.body.lastname,
      captainrank: req.body.captainrank,
      homeplanet: req.body.homeplanet,
    };

    const response = await axios.put(`${captainEndpoint2}/put/${id}`, updatedCaptain);

    res.status(200).json(response.data);
  } catch (error) {
    console.error(error);
    res.status(500).send('Server Error');
  }
});

// route to DELETE captain by ID

const captainEndpoint4 = 'http://127.0.0.1:5000/api/captain/';

app.delete('/cargo/:id', async (req, res) => {
  try {
    const captainId = req.params.id;
    const response = await axios.delete(captainEndpoint4 + captainId);

    res.json(response.data);
  } catch (error) {
    console.error(error);
    res.status(500).send('Server Error');
  }
});

//Spaceship page
app.get('/spaceship', (req, res) => {
  // Make a request to the backend to get spaceship data
  axios.get('http://127.0.0.1:5000/api/spaceship')
    .then(response => {
      res.render('spaceship', { spaceship: response.data });
      console.log(response.data);
    })
    .catch(error => {
      console.error(error);
      res.status(500).send('Error fetching spaceship data');
    });
});

// Route to handle the captain form submission
app.post('/spaceship', async function(req, res) {
  const newSpaceship = {
    maxweight: req.body.maxweight,
    captainid: req.body.captainid,
  };

  const response = await axios.post('http://127.0.0.1:5000/api/spaceship/post', newSpaceship);
  res.status(200).json(response.data);

});

//Delete
const spaceshipEndpoint2 = 'http://127.0.0.1:5000/api/spaceship/';
app.delete('/cargo/:id', async (req, res) => {
  try {
    const spaceshipid = req.params.id;
    const response = await axios.delete(captainEndpoint2 + spaceshipid);

    res.json(response.data);
  } catch (error) {
    console.error(error);
    res.status(500).send('Server Error');
  }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
