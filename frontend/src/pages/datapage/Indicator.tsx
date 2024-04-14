import { useEffect, useState } from "react"
import custom from "./Indicator.module.css"
import Pagination from '@mui/material/Pagination'
import axios from "axios"

interface dataArr {
    traffic: dataF[]
}

interface dataF {
    id: number,
    time_stamp: string,
    source_ip: string,
    destination_ip: string,
    protocol: string,
    port: string,
    packet_size: string,
    prediction: string,
}

function Indicator() {

    const [page, setPage] = useState(1)
    const [data, setData] = useState<dataArr>({
        traffic: []
    })
    useEffect(() => {
        async function fetchData() {
            try {
                await axios.get("https://run.mocky.io/v3/7ef4470c-fe90-4abf-a467-0e7ebed99e46")
                    .then(res => res.data)
                    .then(res => setData(res))
            } catch (error) {
                console.error('Error fetching data:', error);
            }
        }
        fetchData()

        const interval = setInterval(fetchData, 1000);

        return () => clearInterval(interval);
    }, [])

    function handleChangePage(e: Event, p: number) {
        console.log(e)
        setPage(p)
    }
    return (
        <div className={custom.main}>
            <div className={custom.title}>
                <h1>Отслеживание вашего трафика </h1>
                <Pagination onChange={handleChangePage} page={page} count={data.traffic?.length} variant="outlined" color="primary" />
            </div>

            <ul>
                {
                    data?.traffic
                        ?.filter(item => item.id === page)
                        .map(res => (
                            <>
                                <li>
                                    <p>time_stamp: {res?.time_stamp}</p>
                                </li>
                                <li><p>source_ip: {res?.source_ip}</p></li>
                                <li><p>destination_ip: {res?.destination_ip}</p></li>
                                <li><p>protocol: {res?.protocol}</p></li>
                                <li><p>port: {res?.port}</p></li>
                                <li><p>packet_size: {res?.packet_size}</p></li>
                                <li><p>prediction: {res?.prediction}</p></li>
                            </>
                        ))
                }
            </ul>
        </div>
    )
}

export default Indicator