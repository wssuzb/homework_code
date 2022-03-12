using LaTeXStrings
using Plots
gr()


function FastSlowWave(Vₐ::Float64, Cₛ::Int, θ₀::Array, mode::String)
    if mode == "fast"
       strength = sqrt.(1/2 .* (Vₐ ^2 + Cₛ ^2 .+ sqrt.((Vₐ^2 + Cₛ^2) ^2 .- 4 * Vₐ^2 .* Cₛ^2 .* (cos.(θ₀)).^2)))
    end
    if mode == "slow"
       strength = sqrt.(1/2 .* (Vₐ ^2 + Cₛ ^2 .- sqrt.((Vₐ^2 + Cₛ^2) ^2 .- 4 * Vₐ^2 .* Cₛ^2 .* (cos.(θ₀)).^2)))
    end
    return strength
 end
 
l = @layout([a b c])
θ₀ = collect(range(0, 2π, length = 1000))
p1 = plot(θ₀, FastSlowWave(sqrt(1/2), 1, θ₀, "fast"),color=:black, proj=:polar,label=L"\rm{Fast}")
p1 = plot!(θ₀, FastSlowWave(sqrt(1/2), 1, θ₀, "slow"),color=:purple, proj=:polar, label=L"\rm{Slow}")
p1 = plot!(θ₀, 1 * abs.(cos.(θ₀)), proj=:polar, color=:royalblue,label=L"\rm{Alfven}")
p1 = plot!([0,0],[-2,2],proj=:polar, arrow=true,color=:black,linewidth=2,label="")
p1 = annotate!([(1, -0.1, text(L"H"))])
p1 = annotate!([(0.6, -0.1, text(L"1"))])

p2 = plot(θ₀, FastSlowWave(1.0, 1, θ₀, "fast"), color=:black, proj=:polar, label=L"\rm{Fast}")
p2 = plot!(θ₀, FastSlowWave(1.0, 1, θ₀, "slow"), color=:purple, proj=:polar,  label=L"\rm{Slow}")
p2 = plot!(θ₀, 1 * abs.(cos.(θ₀)), proj=:polar, color=:royalblue,label=L"\rm{Alfven}")
p2 = plot!([0,0],[-2,2],proj=:polar, arrow=true,color=:black,linewidth=2,label="")
p2 = annotate!([(1, -0.1, text(L"H"))])
p2 = annotate!([(0.6, -0.1, text(L"1"))])

p3 = plot(θ₀, FastSlowWave(sqrt(2), 1, θ₀, "fast"), color=:black, proj=:polar, label=L"\rm{Fast}")
p3 = plot!(θ₀, FastSlowWave(sqrt(2), 1, θ₀, "slow"),color=:purple, proj=:polar,  label=L"\rm{Slow}")
p3 = plot!(θ₀, 1 * abs.(cos.(θ₀)), proj=:polar, color=:royalblue, label=L"\rm{Alfven}")
p3 = plot!([0,0],[-2,2],proj=:polar, arrow=true, color=:black,linewidth=2,label="")
p3 = annotate!([(1, -0.1, text(L"H"))])
p3 = annotate!([(0.6, -0.1, text(L"1"))])


plot(p1, p2, p3, layout=l,lims=(0,2), ticks =:nothing, border=:none, legend=:topright, xaxis=false, yaxis=false, framestyle = :none, title=[L"(a) s=0.5" L"(b) s=1" L"(c) s=2"])
plot!(size=(1000,300))

savefig("./wave.pdf")
 
 