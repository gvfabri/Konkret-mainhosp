import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Card, CardContent, CardHeader } from "@/components/ui/card"
import { useState } from "react"
import apiClient from "@/api/ApiClient"



function Home() {
  const [name, setName] = useState('')
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [phone, setPhone] = useState('')

  async function registerUser() {

    await apiClient.user.addUserUserPost({
      name: name,
      phone: phone,
      email: email,
      password: password
    }).then(response => {
      setName('')
      setEmail('')
      setPassword('')
      setPhone('')
      console.log(response.data)
    }).catch(error => {
      console.log(error)
    })
  }


  return (
    <div className="min-h-screen bg-white flex items-center justify-center p-4">
      <Card className="w-full max-w-sm border-none shadow-none">
        <CardHeader className="space-y-2">
          <div className="flex items-center justify-between">
            <h1 className="text-2xl font-bold">Bem Vindo</h1>
            <div className="relative w-24 h-24">
              <img
                src="/placeholder.svg?height=96&width=96"
                alt="Illustration"
                width={96}
                height={96}
                className="object-contain"
              />
            </div>
          </div>
          <h2 className="text-xl font-semibold text-blue-600">Login</h2>
        </CardHeader>
        <CardContent className="space-y-4">
          <div className="space-y-4">
            <Input
              className="border-gray-300"
              id="name"
              placeholder="Nome"
              type="text"
              value={name}
              onChange={(e) => setName(e.target.value)}
            />
            <Input
              className="border-gray-300"
              id="password"
              placeholder="Senha"
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
            />
            <div className="text-right">
              <a
                className="text-sm text-gray-600 hover:text-gray-900"
                href="#"
              >
                Esqueceu a senha?
              </a>
            </div>
          </div>
          <Button className="w-full bg-blue-600 hover:bg-blue-700 text-white">
            Login
          </Button>
          <div className="text-center text-sm text-gray-600">
            Não tem uma conta?{" "}
            <a className="text-blue-600 hover:text-blue-700" href="#">
              Criar conta
            </a>
          </div>
        </CardContent>
      </Card>
      <div className="fixed bottom-0 left-0 right-0 h-1/3 bg-blue-600 transform -skew-y-6 origin-bottom-right z-[-1]" />
    </div>
  )
}

export default Home