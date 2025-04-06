import "./Button.scss"

const iconsObject = {
  message: <svg width="18" height="18" viewBox="0 0 18 18" fill="none" xmlns="http://www.w3.org/2000/svg">
  <path d="M16.5 11.5C16.5 11.942 16.3244 12.366 16.0118 12.6785C15.6993 12.9911 15.2754 13.1667 14.8333 13.1667H4.83333L1.5 16.5V3.16667C1.5 2.72464 1.67559 2.30072 1.98816 1.98816C2.30072 1.67559 2.72464 1.5 3.16667 1.5H14.8333C15.2754 1.5 15.6993 1.67559 16.0118 1.98816C16.3244 2.30072 16.5 2.72464 16.5 3.16667V11.5Z" stroke="#1E1E1E" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
  </svg>,
  edit: <svg width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
  <path d="M9.16675 3.3332H3.33341C2.89139 3.3332 2.46746 3.50879 2.1549 3.82135C1.84234 4.13391 1.66675 4.55784 1.66675 4.99986V16.6665C1.66675 17.1086 1.84234 17.5325 2.1549 17.845C2.46746 18.1576 2.89139 18.3332 3.33341 18.3332H15.0001C15.4421 18.3332 15.866 18.1576 16.1786 17.845C16.4912 17.5325 16.6667 17.1086 16.6667 16.6665V10.8332M15.4167 2.0832C15.7483 1.75168 16.1979 1.56543 16.6667 1.56543C17.1356 1.56543 17.5852 1.75168 17.9167 2.0832C18.2483 2.41472 18.4345 2.86436 18.4345 3.3332C18.4345 3.80204 18.2483 4.25168 17.9167 4.5832L10.0001 12.4999L6.66675 13.3332L7.50008 9.99986L15.4167 2.0832Z" stroke="#1E1E1E" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
  </svg>,
}

export default function Button({children, typeButton, color, innerIcon = false}){
  return(
    <button className={color ? `button ${color}` : "button"} type={typeButton}>
      {innerIcon ? iconsObject[innerIcon] : children}
    </button>
  )
}