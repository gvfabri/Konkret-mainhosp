import React, { useEffect, useState } from "react";
import { View, Text, StyleSheet, FlatList } from "react-native";
import { projects_styles } from "@/src/styles/dashboard_styles";
import apiClient from "@/src/api/ApiClient";
import AsyncStorage from "@react-native-async-storage/async-storage";

interface ProjectData {
  name: string;
  start_date: string;
  zip_code?: string;
  state?: string;
  neighborhood?: string;
  public_place?: string;
}

export default function Projects() {
  const [projects, setProjects] = useState<ProjectData[]>([]);

  // Função para buscar os projetos
  async function getProjects() {
    const token = await AsyncStorage.getItem("authToken");
    apiClient.work
      .getallWorksWorkGet({ headers: { Authorization: `Bearer ${token}` } })
      .then((response) => {
        if (response && response.status === 200) {
          const fetchedProjects = response.data;

          setProjects(
            fetchedProjects.map((project: any) => ({
              name: project.name,
              start_date: project.start_date,
              zip_code: project.zip_code || "Não informado",
              state: project.state || "Não informado",
              neighborhood: project.neighborhood || "Não informado",
              public_place: project.public_place || "Não informado",
            }))
          );
        }
      })
      .catch((error) => console.error("Erro ao buscar projetos:", error));
  }

  // UseEffect para carregar os projetos quando o componente é montado
  useEffect(() => {
    getProjects();
  }, []);

  // Renderizar cada projeto em um quadrado
  const renderProject = ({ item }: { item: ProjectData }) => (
    <View style={styles.projectBox}>
      <Text style={styles.projectName}>Nome: {item.name}</Text>
      <Text style={styles.projectInfo}>Data de Início: {item.start_date}</Text>
      <Text style={styles.projectInfo}>CEP: {item.zip_code}</Text>
      <Text style={styles.projectInfo}>Estado: {item.state}</Text>
      <Text style={styles.projectInfo}>Bairro: {item.neighborhood}</Text>
      <Text style={styles.projectInfo}>Logradouro: {item.public_place}</Text>
    </View>
  );

  return (
    <View style={projects_styles.container}>
      <Text style={projects_styles.header}>Projetos:</Text>
      <Text style={projects_styles.subHeader}>Em aberto</Text>
      <FlatList
        data={projects}
        keyExtractor={(item, index) => index.toString()} // Usando o índice como chave temporária
        renderItem={renderProject}
        contentContainerStyle={styles.listContainer}
      />
    </View>
  );
}

// Estilos adicionais
const styles = StyleSheet.create({
  listContainer: {
    paddingVertical: 10,
  },
  projectBox: {
    backgroundColor: "#f5f5f5",
    borderRadius: 8,
    padding: 15,
    marginBottom: 10,
    shadowColor: "#000",
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.2,
    shadowRadius: 2,
    elevation: 3,
  },
  projectName: {
    fontSize: 16,
    fontWeight: "bold",
    marginBottom: 5,
  },
  projectInfo: {
    fontSize: 14,
    color: "#555",
    marginBottom: 3,
  },
});