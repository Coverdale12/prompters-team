import "./DropList.scss"

export default function DropList({ id, children, labelText }) {

  return (
    <div className="droplist">
      {labelText && <label htmlFor={id} className="droplist__label">{labelText}</label> }
      <select name={id} id={id} className="droplist__input">
        {Object.keys(children).map((key) => (
          <option value={key}>
            {children[key]}
          </option>
        ))}
      </select>
    </div>
  )
}