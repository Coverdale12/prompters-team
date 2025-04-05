import "./Checkbox.scss"

export default function Checkbox({id, children}){
  return(
    <div className="checkbox">
      <input type="checkbox" id={id} className="checkbox__input" />
      <label htmlFor={id} className="checkbox__label">{children}</label>
    </div>
  )
}