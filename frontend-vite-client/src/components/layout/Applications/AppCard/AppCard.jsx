import "./AppCard.scss"
import Button from "../../../ui/Button/Button"

export default function AppCard({ children }) {
  return (
    <article className="app-card">
      <header className="app-card__header">
        <h2 className="app-card__title">
          Заявка {children.id}
        </h2>
        <Button innerIcon="message"></Button>

        <Button innerIcon="edit"></Button>
      </header>
      <div className="app-card__body">
        <h3 className="app-card__name">
          {children.name}
        </h3>
        <div className="app-card__money">
          <svg width="70" height="70" viewBox="0 0 36 35" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M28.9474 8.88888V3.72222C28.9474 3.26546 28.7699 2.82741 28.4541 2.50443C28.1382 2.18145 27.7098 2 27.2632 2H5.36842C4.47506 2 3.61829 2.3629 2.98659 3.00885C2.35489 3.65481 2 4.53092 2 5.44444C2 6.35796 2.35489 7.23407 2.98659 7.88003C3.61829 8.52599 4.47506 8.88888 5.36842 8.88888H30.6316C31.0783 8.88888 31.5066 9.07033 31.8225 9.39331C32.1383 9.71629 32.3158 10.1543 32.3158 10.6111V17.5M32.3158 17.5H27.2632C26.3698 17.5 25.513 17.8629 24.8813 18.5088C24.2496 19.1548 23.8947 20.0309 23.8947 20.9444C23.8947 21.8579 24.2496 22.7341 24.8813 23.38C25.513 24.026 26.3698 24.3889 27.2632 24.3889H32.3158C32.7625 24.3889 33.1909 24.2074 33.5067 23.8844C33.8226 23.5615 34 23.1234 34 22.6666V19.2222C34 18.7654 33.8226 18.3274 33.5067 18.0044C33.1909 17.6814 32.7625 17.5 32.3158 17.5Z" stroke="#AFC674" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" />
            <path d="M2 5.44458V29.5557C2 30.4692 2.35489 31.3453 2.98659 31.9913C3.61829 32.6372 4.47506 33.0001 5.36842 33.0001H30.6316C31.0783 33.0001 31.5066 32.8187 31.8225 32.4957C32.1383 32.1727 32.3158 31.7347 32.3158 31.2779V24.389" stroke="#AFC674" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" />
          </svg>
          {children.budget} р.
        </div>
      </div>
      <div className="app-card__table">
        <TableElement keyOrValue={{
          key: "Дата публикации",
          value: children.publish_date
        }} />
        <TableElement keyOrValue={{
          key: "Срок подачи КП",
          value: children.finish_date
        }} />
        <TableElement keyOrValue={{
          key: "Статус",
          value: children.status
        }} />
        <TableElement keyOrValue={{
          key: "Регион",
          value: children.region
        }} />
      </div>
    </article>
  )
}
function TableElement({ keyOrValue }) {
  return (
    <div className="app-card__element">
      {keyOrValue.key}<br />{keyOrValue.value}
    </div>
  )
}