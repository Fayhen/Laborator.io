import Vue from 'vue';
import axios from 'axios';


export const state = Vue.observable({
  isAuthenticated: false,
  user: {
    username: '',
    email: '',
  },
});
// Vue.prototype.$store = { state };

// export const getters = {
//   isAuthenticated: () => state.isAuthenticated,
//   user: () => state.user,
// };

// Getters
export const getAuth = () => state.isAuthenticated;

export const getUser = () => state.user;

// Mutations
export const setAuth = (isLogged) => {
  state.isAuthenticated = isLogged;
};

export const setUser = (user) => {
  state.user = user;
};

// Actions
export const fetchUser = () => {
  axios.get('/auth/user')
    .then((res) => {
      const user = {
        username: res.data.username,
        email: res.data.email,
      };
      setUser(user);
    })
    .catch((err) => {
      console.log(err);
    });
};

export const update = (_where) => {
  if (_where) {
    console.log(`Called update() from ${_where}`);
  }
  if (localStorage.token) {
    const token = JSON.parse(localStorage.token);
    axios.defaults.headers.common.Authorization = `Bearer ${token}`;
    setAuth(true);
    fetchUser();
  } else {
    setAuth(false);
    const user = {
      username: '',
      email: '',
    };
    setUser(user);
  }
};

export const logout = () => {
  localStorage.clear();
  update('Logout action inside the store.');
};
