import * as React from 'react'
import { createLazyFileRoute, useNavigate } from '@tanstack/react-router'
import { Input } from '@/components/ui/input'
import { Button } from '@/components/ui/button'
import apiClient from '@/api/ApiClient'
import { register } from 'module'
import { ArrowLeft } from 'lucide-react'

export const Route = createLazyFileRoute('/signupCPF')({
  component: SignupCPF,
})

function SignupCPF() {
  const navigation = useNavigate()
  const [formData, setFormData] = React.useState({
    name: '',
    cpf: '',
    email: '',
    password: '',
    confirmPassword: ''
  })

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setFormData({ ...formData, [e.target.name]: e.target.value })
  }

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault()
    console.log('Form submitted:', formData)
  }

    async function registerUser() {

      await apiClient.user.addUserUserPost({
        name: formData.name,
        cpf: formData.cpf,
        email: formData.email,
        password: formData.password
      }).then(response => {
        setFormData({
          name: '',
          cpf: '',
          email: '',
          password: '',
          confirmPassword: '',
        })
        console.log(response.data)
        navigation({ to: '/'})
      }).catch(error => {
        console.log(error)
      })
    }

  return (
    <div className="min-h-screen bg-white flex flex-col">
      <div className="h-32 bg-blue-600 relative overflow-hidden">
        <div className="absolute top-0 right-0 w-1/2 h-full bg-yellow-400 rounded-bl-[100%]" />
      </div>
      <div className="flex-grow bg-white rounded-t-3xl -mt-6 px-6 py-8">
        <div className="max-w-md mx-auto">
          <h1 className="text-3xl font-bold text-blue-600 mb-1">Criar Conta</h1>
          <h2 className="text-xl text-blue-600 mb-6">Física:</h2>
          <form onSubmit={handleSubmit} className="space-y-4">
          <Button variant="ghost" className="w-10 h-10 p-0 absolute top-4 left-4" onClick={()=>navigation({ to: '/signup'})}>
            <ArrowLeft className="h-6 w-6 text-white" />
          </Button>
            
            <Input
              name="name"
              value={formData.name}
              onChange={handleChange}
              placeholder="Nome"
              className="h-12 rounded-lg border-gray-300"
            />
            <Input
              name="cpf"
              value={formData.cpf}
              onChange={handleChange}
              placeholder="CPF"
              className="h-12 rounded-lg border-gray-300"
            />
            <Input
              name="email"
              type="email"
              value={formData.email}
              onChange={handleChange}
              placeholder="E-mail"
              className="h-12 rounded-lg border-gray-300"
            />
            <Input
              name="password"
              type="password"
              value={formData.password}
              onChange={handleChange}
              placeholder="Senha"
              className="h-12 rounded-lg border-gray-300"
            />
            <Input
              name="confirmPassword"
              type="password"
              value={formData.confirmPassword}
              onChange={handleChange}
              placeholder="Confirmar senha"
              className="h-12 rounded-lg border-gray-300"
            />
            <Button type="submit" className="w-full h-12 mt-6 text-lg font-medium bg-blue-600 hover:bg-blue-700 rounded-lg" onClick={registerUser}>  
              Criar Conta
            </Button>
          </form>
        </div>
      </div>
    </div>
  )
}
