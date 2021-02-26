import Link from 'next/link';
import {Box, Container} from "@material-ui/core";
import theme from '@/styles/theme';
import menu from '@/store/menu';
import styles from './Header.module.scss'

export default function Header(){
    return(
        <header>
            <Box
                p={3}
                style={{
                    backgroundColor: theme.palette.primary.main
                }}
            >
                <Container>
                    <nav>
                        <ul className={styles.menu}>
                            {menu.map(item=>{
                                return(
                                    <li
                                        key={item.link}
                                        className={styles.link}
                                    >
                                        <Link
                                            href={item.link}
                                        >
                                            <a
                                                style={{
                                                    color: theme.palette.primary.contrastText
                                                }}
                                            >
                                                {item.title}
                                            </a>
                                        </Link>
                                    </li>
                                )
                            })}
                        </ul>
                    </nav>
                </Container>
            </Box>
        </header>
    )
}