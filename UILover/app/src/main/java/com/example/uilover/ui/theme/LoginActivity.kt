package com.example.uilover

import android.content.Intent
import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import com.example.uilover.databinding.ActivityLoginBinding

class LoginActivity : AppCompatActivity() {
    private lateinit var binding: ActivityLoginBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityLoginBinding.inflate(layoutInflater)
        setContentView(binding.root)

        binding.tvSignup.setOnClickListener {
            startActivity(Intent(this, SignupActivity::class.java))
        }

        binding.btnLogin.setOnClickListener {
            // TODO: Implement login logic
        }
    }
}
