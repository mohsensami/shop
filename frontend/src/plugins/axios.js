import axios from 'axios'

const axiosInstance = axios.create({
  baseURL: 'http://localhost:8000',
  withCredentials: false,
  headers: {
    // Accept: "application/json",
    "Content-Type": "multipart/form-data",
  },
})

// if (localStorage.getItem('token')) {
//   axiosInstance.defaults.headers['Authorization'] = 'Bearer ' + localStorage.getItem('token')
// }

export default axiosInstance