import { styles } from "../../src/styles";
import { Link } from "expo-router";
import { Pressable, TextInput } from "react-native-gesture-handler";
import { Text, View } from "react-native";




export default function NewUser() {
    return (
        <View style={styles.container}>
            <View style={styles.loginBox}>
                <Text style={styles.formTitle}>Pessoa Jurídica</Text>
                <TextInput
                    style={styles.formInput}
                    placeholder="Nome"
                    autoCapitalize="none"
                />
                <TextInput
                    style={styles.formInput}
                    placeholder="Senha"
                    autoCapitalize="none"
                    secureTextEntry
                />
                <TextInput
                    style={styles.formInput}
                    placeholder="CPF"
                    autoCapitalize="none"
                />
                <TextInput
                    style={styles.formInput}
                    placeholder="E-Mail"
                    autoCapitalize="none"
                />
                <Link href="/user_register/register_options" style={styles.subButton}>
                    <Text style={styles.subTextButton}>Voltar</Text>
                </Link>
            </View>
        </View>
    )
}