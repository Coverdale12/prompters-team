import { useState } from 'react'


// Components
import Login from './components/pages/Login/Login'

function App() {
  const [count, setCount] = useState(0)

  return (
    <Login></Login>
  )
}

export default App
