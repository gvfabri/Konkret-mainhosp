import { Link, Stack } from "expo-router";
import { StatusBar } from "expo-status-bar";
import { Pressable, TextInput, View, Text } from "react-native";
import { styles } from '../src/styles';

export default function RootLayout() {
  return (
    <View style={styles.container}>
      <View style={styles.loginBox}>
        <Text style={styles.formTitle}>Login no Sistema</Text>
        <TextInput
          style={styles.formInput}
          placeholder="Informe o E-Mail"
          keyboardType="email-address"
          autoCapitalize="none"
          autoComplete="email"
        />
        <TextInput
          style={styles.formInput}
          placeholder="Informe a Senha"
          autoCapitalize="none"
          secureTextEntry
        />
        <Pressable style={styles.formButton}>
          <Text style={styles.textButton}>Logar</Text>
        </Pressable>
        <View style={styles.subContainer}>
          <Pressable style={styles.subButton}>
            <Text style={styles.subTextButton}>Esqueci a senha</Text>
          </Pressable>
          <Link href="/new-user" style={styles.subButton}>
            <Text style={styles.subTextButton}>Novo usuário</Text>
          </Link>
        </View>
      </View>
      <StatusBar style="auto" />
    </View>
  );
}
