import "./Preview.scss"
import logoIcon from "../../../assets/icons/logo/icon-logo.svg"

import Logotype from "../../layout/Logotype/Logotype"
import Button from "../../ui/Button/Button"


export default function Preview() {
  return (
    <main className="content">
      <section className="preview">
        <div className="preview__wrapper container">
          <Logotype />
          <div className="preview__body">
            <h1 className="preview__title">Идея на миллион?<span className="preview__title mini">Пришло время действовать!</span></h1>
            <img src="/images/woman.png" alt="Женщина" className="preview__image"/>
          </div>
          <Button color="purple">Перейти</Button>
        </div>
      </section>
    </main>
  )
}