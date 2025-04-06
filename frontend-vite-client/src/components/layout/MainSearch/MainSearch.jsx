import "./MainSearch.scss"


export default function MainSearch() {
  return(
    <div className="field-search">
      <label htmlFor="mainSearch" className="field-search__label visually-hidden">
        Поиск по меню
      </label>
      <input 
        type="search" 
        id="mainSearch" 
        placeholder="Поиск(по меню)" 
        className="field-search__input"/>
    </div>
  )
}