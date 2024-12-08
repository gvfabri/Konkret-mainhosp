import { styles } from "@/src/styles";
import { Link } from "expo-router";
import { Pressable, TextInput } from "react-native-gesture-handler";
import { Text, View } from "react-native";




export default function NewUser() {
    return (
        <View style={styles.container}>
            <View style={styles.loginBox}>
                <Text style={styles.formTitle}>Criar novo usuário</Text>
                <TextInput
                    style={styles.formInput}
                    placeholder="Nome"
                    autoCapitalize="words"
                />
                <TextInput
                    style={styles.formInput}
                    placeholder="E-mail"
                    keyboardType="email-address"
                    autoCapitalize="none"
                    autoComplete="email"
                />
                <TextInput
                    style={styles.formInput}
                    placeholder="Senha"
                    autoCapitalize="none"
                    secureTextEntry
                />
                <Pressable style={styles.formButton}>
                    <Text style={styles.textButton}>Criar conta</Text>
                </Pressable>
                <Link href="/" style={styles.subButton}>
                    <Text style={styles.subTextButton}>Voltar para o Login</Text>
                </Link>
            </View>
        </View>
    )
}