import "./Button.scss"

export default function Button({children, typeButton}){
  return(
    <button className="button" type={typeButton}>
      {children}
    </button>
  )
}