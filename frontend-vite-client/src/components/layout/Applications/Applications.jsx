import AppCard from "./AppCard/AppCard"
import { objectStartUpEmulator } from "./startup" //Эмулятор данных с бэка
import "./Applications.scss"

export default function Applications() {

  return (
    <section className="applications">
      <div className="applications__wrapper">
        <ul className="applications__list">
          {objectStartUpEmulator.map((card) => (
            <li className="applications__item" key={card.id}>
              <AppCard>{card}</AppCard>
            </li>
          ))}
        </ul>
      </div>
    </section>
  )
}