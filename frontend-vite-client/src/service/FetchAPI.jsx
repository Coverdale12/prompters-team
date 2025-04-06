import axios from "axios"

const urlAPI = "http://localhost:8000"

export async function loginAPI(email, password) {
  try {
    const response = await axios.post(`${urlAPI}/authorization/auth`, {
      email,
      password
    }, {
      headers: {
        "Content-Type": 'application/json'
      }
    })
    
    return response.data
  } catch (error) {
    throw error
  }
}