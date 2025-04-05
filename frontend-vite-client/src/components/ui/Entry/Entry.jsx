import "./Entry.scss"

export default function Entry({id, labelText, placeholderText, typeEntry = "text"}){
  return(
    <div className="entry">
      <label htmlFor={id} className="entry__label">
        {labelText}
      </label>
      <input className="entry__input" placeholder={placeholderText} type={typeEntry} name={id} id={id} />
      <div className="entry__error">
      </div>
    </div>
  )
}