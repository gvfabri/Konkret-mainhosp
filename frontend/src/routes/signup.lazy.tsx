import * as React from 'react'
import { Button } from '@/components/ui/button'
import { createLazyFileRoute, useNavigate } from '@tanstack/react-router'
import { ArrowLeft, Home } from 'lucide-react'

export const Route = createLazyFileRoute('/signup')({
  component: SignupOptions,
})

function SignupOptions() {
  const navigation = useNavigate()
  return (
    <div className="h-screen w-full bg-white overflow-hidden relative">
      {/* Yellow curved shape */}
      <div className="absolute top-0 left-0 right-0 h-1/3 bg-yellow-400 rounded-b-[50%] z-0"></div>
      
      {/* Blue wave shape */}
      <div className="absolute top-12 left-0 right-0 h-1/4 bg-blue-600 rounded-t-[50%] z-10"></div>
      
      {/* Content container */}
      <div className="relative z-20 h-full flex flex-col p-6">
        {/* Back button */}
        <Button variant="ghost" className="w-10 h-10 p-0 absolute top-4 left-4" onClick={()=>navigation({ to: '/'})}>
          <ArrowLeft className="h-6 w-6 text-white" />
        </Button>
        
        {/* Main content */}
        <div className="flex-grow flex flex-col items-center justify-center space-y-8">
          <h1 className="text-2xl font-bold text-blue-600">Criar conta como:</h1>
          
          {/* Placeholder for the illustration */}
          <div className="w-64 h-64 bg-gray-200 rounded-full flex items-center justify-center">
            <span className="text-gray-400">Illustration</span>
          </div>
          
          {/* Buttons */}
          <div className="space-y-4 w-full max-w-xs">
            <Button className="w-full bg-blue-600 hover:bg-blue-700 text-white" onClick={()=>navigation({ to: '/signupCPF'})}>
              Pessoa Física
            </Button>
            <Button className="w-full bg-yellow-400 hover:bg-yellow-500 text-blue-600">
              Pessoa Jurídica
            </Button>
          </div>
        </div>
      </div>
    </div>
  )
}
