import "./Logotype.scss"
import { Link } from "react-router"
import iconLogo from "../../../assets/icons/logo/icon-logo.svg"


export default function Logotype(path=""){
  return(
    <Link to={path} className="logotype">
      <img src={iconLogo} alt="granter logo" className="logotype__image"/>
      <h1 className="logotype__title">
        Granter
      </h1>
    </Link>
  )
}