import { styles } from "../../src/styles/login_styles";
import { Link } from "expo-router";
import { Text, View } from "react-native";




export default function NewUser() {
    return (
        <View style={styles.container}>
            <View style={styles.loginBox}>
                <Text style={styles.formTitle}>Criar novo usuário</Text>
                <Link href="/user_register/pessoa_fisica" style={styles.formButton}>
                    <Text style={styles.textButton}>Pessoa física</Text>
                </Link>
                <Link href="/user_register/pessoa_juridica" style={styles.formButton}>
                    <Text style={styles.textButton}>Pessoa jurídica</Text>
                </Link>
                <Link href="/" style={styles.subButton}>
                    <Text style={styles.subTextButton}>Voltar para o Login</Text>
                </Link>
            </View>
        </View>
    )
}