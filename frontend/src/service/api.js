import axios from 'axios';

const CONFIG = {
  baseURL: 'http://localhost:5001',
  timeout: 5000,
  headers: { Accept: 'application/json' },
};

export const get = (path, config = {}) => {
  return axios
    .get(path, { ...CONFIG, ...config })
    .then((response) => response.data);
};

export const post = (path, data = {}, config = {}) => {
  return axios
    .post(path, data, { ...CONFIG, ...config })
    .then((response) => response.data);
};

export const put = (path, data = {}, config = {}) => {
  return axios
    .put(path, data, { ...CONFIG, ...config })
    .then((response) => response.data);
};

export const patch = (path, data = {}, config = {}) => {
  return axios
    .patch(path, data, { ...CONFIG, ...config })
    .then((response) => response.data);
};

export const httpDelete = (path, config = {}) => {
  return axios
    .delete(path, { ...CONFIG, ...config })
    .then((response) => response.data);
};
