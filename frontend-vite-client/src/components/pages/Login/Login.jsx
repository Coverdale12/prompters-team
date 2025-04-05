import "./Login.scss"
// components
import Entry from "../../ui/Entry/Entry"
import Button from "../../ui/Button/Button"
import DropList from "../../ui/DropList/DropList"
import Checkbox from "../../ui/Checkbox/Checkbox"

import { useState } from "react"

// react-router
import { Link } from "react-router"

export default function Login() {
  const [isWindow, setIsWindow] = useState(false)

  
  return (
    <section className="section login">
      <div className="login__wrapper container">
        <nav className="login__navigation">
          <button className={`login__navigation button ${isWindow && "active"}`}
            onClick={(e) => {
              setIsWindow(true)
              changeWindow(e)
            }}>
            Регистрация
          </button>
          <button className={`login__navigation button ${!isWindow && "active"}`}
            onClick={(e) => {
              setIsWindow(false)
              changeWindow(e)
            }}>
            Авторизация
          </button>
        </nav>
        {isWindow ? <RegistrationForm /> : <LoginForm />}

      </div>
    </section>
  )
}

function RegistrationForm() {
  return (
    <form action="" className="form login">
      <DropList id="typeUser" labelText="Я">{{
        executor: "Исполнитель",
        customer: "Заказчик"
      }}</DropList>
      <Entry
        id="email"
        labelText="Введите почту"
        placeholderText="mail@example.com" />
      <Entry
        id="password"
        typeEntry="password"
        labelText="Введите пароль"
        placeholderText="password123" />
      <Checkbox id="agreement">Согласие на обработку персональных данных</Checkbox>
      <Button typeButton="submit">
        Отправить
      </Button>
    </form>
  )
}
function LoginForm() {
  return (
    <form action="" className="form login">
      <Entry
        id="email"
        labelText="Введите почту"
        placeholderText="mail@example.com" />
      <Entry
        id="password"
        typeEntry="password"
        labelText="Введите пароль"
        placeholderText="password123" />
      <Button typeButton="submit">
        Войти
      </Button>
    </form>
  )
}