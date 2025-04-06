import "./StartApp.scss"

// components
import Entry from "../../ui/Entry/Entry"
import DropList from "../../ui/DropList/DropList"

export default function StartApp(){
  return(
    <section className="start-app">
      <div className="start-app__wrapper container">
        <form className="form">
          <DropList></DropList>
          <Entry ></Entry>
        </form>
      </div>
    </section>
  )
}