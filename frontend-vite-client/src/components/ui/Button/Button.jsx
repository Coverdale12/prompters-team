import "./Button.scss"

export default function Button({children, typeButton, color}){
  return(
    <button className={color ? `button ${color}` : "button"} type={typeButton}>
      {children}
    </button>
  )
}