import AppCard from "./AppCard/AppCard"
import { objectStartUpEmulator } from "./startup" //Эмулятор данных с бэка
import "./Applications.scss"
import { useEffect, useState } from "react"
import { getStartAppCards } from "../../../service/FetchAPI"


export default function Applications() {
  const [appList, setAppList] = useState([])
  useEffect(() => {
    getStartAppCards().then((data) => {
      const massive = data.startups 
      if(massive.length == 0){
        setAppList(false)
        return
      }
      setAppList(data.startups)
    }).catch((err) => {
      console.log(err)
    })
  }, [])
  return (
    <section className="applications">
      <div className="applications__wrapper">
        <ul className="applications__list">
          {appList ? appList.map((card) => (
            <li className="applications__item" key={card.id}>
              <AppCard>{card}</AppCard>
            </li>
          )) : <p className="error-log">Заявок пока нету!</p>}
        </ul>
      </div>
    </section>
  )
}