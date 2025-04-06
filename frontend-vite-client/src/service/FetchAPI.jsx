import axios from "axios"

const urlAPI = "http://localhost:8000"

export async function loginAPI(email, password) {
  try {
    const response = await axios.post(`${urlAPI}/authorization/auth/`, {
      email,
      password
    }, {
      headers: {
        "Content-Type": 'application/json'
      }
    })
    if (response.status === 401){
      throw "401"
    }
    return response.data
  } catch (error) {
    throw error
  }
}
export async function getStartAppCards() {
  try {
    const response = await axios.get(`${urlAPI}/main/startups/`, {
      headers: {
        "Content-Type": 'application/json'
      }
    })
    if (response.status === 401){
      throw "401"
    }
    return response.data
    
  } catch (error) {
    throw error
  }
}