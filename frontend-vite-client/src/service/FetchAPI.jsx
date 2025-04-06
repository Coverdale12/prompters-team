import axios from "axios"

const urlAPI = window.location.hostname

export async function loginAPI(email, password) {
  try {
    const response = await axios.post(`${urlAPI}/auth`, {
      email: email,
      password: password
    })
    
    
  } catch (error) {
    
  }
}