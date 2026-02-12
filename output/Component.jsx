
function CreateAccountForm() {
  return (
    <div className="flex h-screen bg-blue-400">
      <div className="w-1/2 bg-blue-300 rounded-r-3xl flex flex-col justify-center items-center">
        <div className="text-white text-2xl mb-4 text-left w-3/4">
          Need webdesign <br />
          for your business?
          <br />
          <span className="text-blue-500 font-bold text-3xl">
            Design Spacee
          </span>
          <br />
          will help you.
        </div>
        <div className="bg-blue-400 rounded-2xl shadow-md w-40 h-40 items-center justify-center flex">
          <span className="text-white text-9xl ">S</span>
        </div>
       <div className=" items-center justify-center mt-10 text-white">
          figma.com/@designspacee
        </div>
      </div>
      <div className="w-1/2 bg-white rounded-l-3xl flex flex-col justify-center items-center">
        <h1 className="text-2xl font-semibold mb-6">Create Account</h1>

        <div className="flex flex-row space-x-4">
          <button className="border border-gray-300 py-2 px-4 rounded hover:bg-gray-100 focus:outline-none">
            Sign up with Google
          </button>
          <button className="border border-gray-300 py-2 px-4 rounded hover:bg-gray-100 focus:outline-none">
            Sign up with Facebook
          </button>
        </div>

        <div className="flex items-center space-x-2 my-4">
          <div className="border-t border-gray-300 w-20"></div>
          <span className="text-gray-500">OR</span>
          <div className="border-t border-gray-300 w-20"></div>
        </div>

        <input
          type="text"
          placeholder="Full Name"
          className="border-b border-gray-300 py-2 px-3 mb-3 w-64 focus:outline-none"
        />
        <input
          type="email"
          placeholder="Email"
          className="border-b border-gray-300 py-2 px-3 mb-3 w-64 focus:outline-none"
        />
        <input
          type="password"
          placeholder="Password"
          className="border-b border-gray-300 py-2 px-3 mb-4 w-64 focus:outline-none"
        />

        <button className="bg-blue-500 text-white py-2 px-4 rounded hover:bg-blue-600 focus:outline-none w-64">
          Create Account
        </button>

        <p className="mt-4 text-sm">
          Already have an account?{" "}
          <a href="#" className="text-blue-500 hover:underline">
            Login
          </a>
        </p>
      </div>
    </div>
  );
}